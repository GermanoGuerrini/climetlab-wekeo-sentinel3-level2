#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

import re

import climetlab as cml
import xarray as xr
from climetlab import Dataset

__version__ = "0.1.0"


def merger(paths):
    print(f"merging {len(paths)} paths.")
    print(paths)
    data_paths = [x for x in paths if re.match(f".*/.*reflectance\.nc$", x)]
    ds = xr.open_mfdataset(data_paths)

    coord_paths = [x for x in paths if x.endswith("/time_coordinates.nc")]
    assert len(coord_paths) == 1, paths
    coord_ds = xr.open_dataset(coord_paths[0])

    # do something to change 'ds' using 'coord_ds'
    # ...
    # something like this maybe?
    # ds[TIME_COORD_NAME] = xr.DataArray(coord_ds.values)
    # ds.set_coords...
    # ...
    # now the ds has coordinates is ready to be merge to another one

    return ds


class Main(Dataset):
    name = None
    home_page = "-"
    # The licence is the licence of the data (not the licence of the plugin)
    licence = "-"
    documentation = "-"
    citation = "-"

    # These are the terms of use of the data (not the licence of the plugin)
    terms_of_use = (
        "By downloading data from this dataset, "
        "you agree to the terms and conditions defined at "
        "https://www.copernicus.eu/en/access-data/copyright-and-licences"
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = None

    inputs = []
    choices = []

    def __init__(
        self,
        *args,
        **kwargs
    ):
        type_ = kwargs["type"]
        area = kwargs["area"]
        start = kwargs["start"]
        end = kwargs["end"]
        query = {
            "datasetId": f"EO:EUM:DAT:SENTINEL-3:{type_}",
            "boundingBoxValues": [
                {
                    "name": "bbox",
                    "bbox": [
                        area[1],
                        area[2],
                        area[3],
                        area[0],
                    ],
                }
            ],
            "dateRangeSelectValues": [
                {"name": "position", "start": f"{start}", "end": f"{end}"}
            ],
        }

        choices = dict(zip(self.choices, [kwargs[c] for c in self.choices]))
        if any(c is not None for c in choices.values()):
            query["stringChoiceValues"] = []

            for choice in choices:
                if choices.get(choice) is not None:
                    query["stringChoiceValues"].append(
                        {"name": choice, "value": choices[choice]}
                    )

        inputs = dict(zip(self.inputs, [kwargs[i] for i in self.inputs]))
        if any(c is not None for c in inputs.values()):
            query["stringInputValues"] = []

            for input in inputs:
                if inputs.get(input) is not None:
                    query["stringInputValues"].append(
                        {"name": input, "value": inputs[input]}
                    )

        # TODO: find the names of these sub-directories
        # or let the "wekeo" source find them
        dirnames = [
            "S3A_OL_2_WFR____20230506T091023_20230506T091323_20230506T112056_0180_098_264_1980_MAR_O_NR_003.SEN3",
            "S3A_OL_2_WFR____20230508T081801_20230508T082101_20230508T102705_0179_098_292_1980_MAR_O_NR_003.SEN3",
        ]

        sources = []
        for root in dirnames:
            filter = lambda x: re.match(f".*/{root}/.*\.nc", x) or x.endswith(".SEN3")
            s = cml.load_source(
                "wekeo",
                query,
                filter=filter,
                merger=merger,  # TODO: the merger function is above, has access to other netcdf.
            )
            sources.append(s)

        self.sources = sources

    def to_xarray(self):
        datasets = [s.to_xarray() for s in self.sources]
        # TODO: make sure the data is concatenable
        print(datasets)
        datasets = [datasets[0]]
        return xr.concat(datasets, dim="time")




