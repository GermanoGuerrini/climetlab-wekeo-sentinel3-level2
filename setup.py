#!/usr/bin/env python
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.


import io
import os

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


package_name = "climetlab_wekeo_sentinel3_level2"  # noqa: E501

version = None
lines = read(f"{package_name}/version").split("\n")
if lines:
    version = lines[0]

assert version


extras_require = {}

setuptools.setup(
    name=package_name,
    version=version,
    description=(
        "A dataset plugin for climetlab for the dataset climetlab-wekeo-sentinel3-level2"  # noqa: E501
    ),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Germano Guerrini",
    author_email="germano.guerrini@exprivia.com",
    url="http://github.com/GermanoGuerrini/climetlab-wekeo-sentinel3-level2",
    license="Apache License Version 2.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["climetlab>=0.10.0"],
    extras_require=extras_require,
    zip_safe=True,
    entry_points={
        "climetlab.datasets": [
            # End-users will use cml.load_dataset("climetlab-wekeo-sentinel3-level2", ...)
            # see the tests/ folder for a example.
            "wekeo-sentinel3-sral-l2-wat=climetlab_wekeo_sentinel3_level2.sral_l2_wat:sral_l2_wat",
            "wekeo-sentinel3-sral-l1-sra-bs=climetlab_wekeo_sentinel3_level2.sral_l1_sra_bs:sral_l1_sra_bs",
            "wekeo-sentinel3-sral-l1-sra-a=climetlab_wekeo_sentinel3_level2.sral_l1_sra_a:sral_l1_sra_a",
            "wekeo-sentinel3-sral-l1-sra=climetlab_wekeo_sentinel3_level2.sral_l1_sra:sral_l1_sra",
            "wekeo-sentinel3-slstrl2-wst=climetlab_wekeo_sentinel3_level2.slstrl2_wst:slstrl2_wst",
            "wekeo-sentinel3-slstrl1-rbt=climetlab_wekeo_sentinel3_level2.slstrl1_rbt:slstrl1_rbt",
            "wekeo-sentinel3-olci-l2-wrr=climetlab_wekeo_sentinel3_level2.olci_l2_wrr:olci_l2_wrr",
            "wekeo-sentinel3-olci-l2-wfr=climetlab_wekeo_sentinel3_level2.olci_l2_wfr:olci_l2_wfr",
            "wekeo-sentinel3-olci-l1-err=climetlab_wekeo_sentinel3_level2.olci_l1_err:olci_l1_err",
            "wekeo-sentinel3-olci-l1-efr=climetlab_wekeo_sentinel3_level2.olci_l1_efr:olci_l1_efr",
            "wekeo-sentinel3-olci-l2-ocrr=climetlab_wekeo_sentinel3_level2.olci_l2_ocrr:olci_l2_ocrr",
            "wekeo-sentinel3-olci-l2-ocfr=climetlab_wekeo_sentinel3_level2.olci_l2_ocfr:olci_l2_ocfr",
            "wekeo-sentinel3-slstr-l2-frp=climetlab_wekeo_sentinel3_level2.slstr_l2_frp:slstr_l2_frp",
            "wekeo-sentinel3-slstr-l2-aod=climetlab_wekeo_sentinel3_level2.slstr_l2_aod:slstr_l2_aod",
           # Other datasets can be included here
            # "climetlab-wekeo-sentinel3-level2-dataset-2= climetlab_wekeo_sentinel3_level2.main2:Main2",  # noqa: E501
        ]
        # source plugins would be here
        # "climetlab.sources": []
    },
    keywords="meteorology",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
