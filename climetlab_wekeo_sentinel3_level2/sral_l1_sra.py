#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations
from climetlab.decorators import normalize

from climetlab_wekeo_sentinel3_level2.main import Main



class sral_l1_sra(Main):
    name = "EO:EUM:DAT:SENTINEL-3:SR_1_SRA___"
    dataset = None
    inputs = [
        "relorbit",
        "orbit",
        "cycle",
    ]
    choices = [
        "sat",
        "type",
        "timeliness",
        "orbitdir",
    ]
    
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("sat", ['Sentinel-3A', 'Sentinel-3B'])
    @normalize("type", ['SR_1_SRA___'])
    @normalize("timeliness", ['NR', 'NT', 'ST'])
    @normalize("orbitdir", ['ASCENDING', 'DESCENDING'])
    @normalize("relorbit")
    @normalize("orbit")
    @normalize("cycle")
    def __init__(
        self,
        area=None,
        start="2021-01-01T00:03:51.085Z",
        end="2023-06-16T07:57:11.287Z",
        sat=None,
        type="SR_1_SRA___",
        timeliness=None,
        orbitdir=None,
        relorbit=None,
        orbit=None,
        cycle=None,
    ):
        super().__init__(
            area=area,
            start=start,
            end=end,
            sat=sat,
            type=type,
            timeliness=timeliness,
            orbitdir=orbitdir,
            relorbit=relorbit,
            orbit=orbit,
            cycle=cycle,
        )
