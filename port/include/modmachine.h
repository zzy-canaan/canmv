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

#ifndef __MOD_MACHINE_H__
#define __MOD_MACHINE_H__

#include "py/obj.h"

struct st_iomux_reg {
    union {
        struct {
            uint32_t st : 1;        // bit 0 输入施密特触发器控制使能
            uint32_t ds : 4;        // bit 4-1 驱动电流控制：
            uint32_t pd : 1;        // bit 5 下拉；
            uint32_t pu : 1;        // bit 6
            uint32_t oe : 1;        // bit 7 out
            uint32_t ie : 1;        // bit 8 input
            uint32_t msc : 1;       // bit 9 电压选择；
            uint32_t sl : 1;        // bit 10  输出翻转率控制使能（双电压PAD无此控制端
            uint32_t io_sel : 3;    // bit 13-11 func 选择
            uint32_t rsv : 17;      // bit 30-14
            uint32_t di : 1;        // bit 31 当前PAD输入到芯片内部的数据(即PAD的C端)
        } bit;
        uint32_t value;
    } u;
};

int fpioa_drv_reg_set(uint32_t pin, uint32_t value);
int fpioa_drv_reg_get(uint32_t pin, uint32_t *value);

int machine_i2c_obj_get_fd(mp_obj_t self_in);

void machine_pin_value_set(mp_obj_t self_in, int value);
int machine_pin_value_get(mp_obj_t self_in);

void machine_pin_mode_set(mp_obj_t self_in, int value);
int machine_pin_mode_get(mp_obj_t self_in);

void machine_pin_pull_set(mp_obj_t self_in, int value);
int machine_pin_pull_get(mp_obj_t self_in);

void machine_pin_drive_set(mp_obj_t self_in, int value);
int machine_pin_drive_get(mp_obj_t self_in);

int machine_pin_get_pin_numer(mp_obj_t self_in);

extern const mp_obj_type_t machine_adc_type;
extern const mp_obj_type_t machine_fft_type;
extern const mp_obj_type_t machine_fpioa_type;
extern const mp_obj_type_t machine_i2c_type;
extern const mp_obj_type_t machine_i2c_slave_type;
extern const mp_obj_type_t machine_led_type;
extern const mp_obj_type_t machine_pin_type;
extern const mp_obj_type_t machine_pwm_type;
extern const mp_obj_type_t machine_rtc_type;
extern const mp_obj_type_t machine_spi_type;
extern const mp_obj_type_t machine_spi_lcd_type;
extern const mp_obj_type_t machine_timer_type;
extern const mp_obj_type_t machine_touch_type;
extern const mp_obj_type_t machine_touch_user_type;
extern const mp_obj_type_t machine_uart_type;
extern const mp_obj_type_t machine_wdt_type;

#endif // __MOD_MACHINE_H__
