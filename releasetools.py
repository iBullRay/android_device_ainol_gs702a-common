#
# Copyright (C) 2012 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Custom OTA commands for mangov2 """

def FullOTA_InstallBegin(info):
  info.script.AppendExtra('mount("vfat", "EMMC", "/dev/block/actb", "/misc");')
  info.script.AppendExtra('package_extract_dir("system/kernel/misc", "/misc");')
  info.script.AppendExtra('unmount("/misc");')