# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
from prophet.forecaster import Prophet
import os

pre_release_version = os.getenv('PRE_RELEASE_VERSION', '')
__version__ = pre_release_version if pre_release_version else '1.1.5'
