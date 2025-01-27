/* Copyright (c) 2023, Canaan Bright Sight Co., Ltd
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 * 1. Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
 * CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
 * INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

DEF_INT_FUNC_INT_STRUCT(kd_mpi_connector_init, k_connector_info)
DEF_INT_FUNC_INT_STRUCTPTR(kd_mpi_connector_id_get, k_u32)
DEF_INT_FUNC_INT_INT(kd_mpi_connector_power_set)
DEF_INT_FUNC_INT(kd_mpi_connector_close)
DEF_INT_FUNC_STR(kd_mpi_connector_open)
DEF_INT_FUNC_INT_STRUCTPTR(kd_mpi_get_connector_info, k_connector_info)

DEF_INT_FUNC_VOID(ide_dbg_vo_wbc_init)
DEF_INT_FUNC_VOID(ide_dbg_vo_wbc_deinit)
DEF_INT_FUNC_INT_INT_INT(ide_dbg_set_vo_wbc)

DEF_INT_FUNC_INT_STRUCTPTR_STRUCTPTR(kd_mpi_vo_osd_rotation, k_video_frame_info, k_video_frame_info)
