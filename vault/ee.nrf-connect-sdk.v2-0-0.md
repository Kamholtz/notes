---
id: dx3j6zht7bpvmddvvsdji36
title: V2 0 0
desc: ''
updated: 1656829592859
created: 1656828716044
---

## Known Issues

[Known issues &mdash; nRF Connect SDK 2.0.0 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/2.0.0/nrf/known_issues.html)

## Migration notes

[Migration notes for nRF Connect SDK v2.0.0 &mdash; nRF Connect SDK 2.0.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/migration/migration_guide_1.x_to_2.x.html)

Required Action:

- [x] pwms properties in devicetree nodes must be extended with two more cells (with period and flags) and now they need to specify PWM channels, not pin numbers.
- [ ] Calls to the deprecated pwm_pin_set_cycles function must be replaced with calls to the pwm_set_cycles() function.
- [ ] Calls to the deprecated pwm_pin_set_usec and pwm_pin_set_nsec functions must be replaced with calls to the pwm_set() function with the period and pulse values wrapped in the PWM_USEC macro or the PWM_NSEC macro, respectively.


## Problems encountered

Reboot occured when a GPIO interrupt was fired.
> I: Unimplemented signal (signal: 54, status: 0)
> I: Joined network successfully on reboot signal (Extended PAN ID: cccccccc9ca8cc84, PAN ID: 0x0c84)
> I: Debounced
> ASSERTION FAIL @ WEST_TOPDIR/nrf/lib/dk_buttons_and_leds/dk_buttons_and_leds.c:186
> E: r0/a1:  0x00000004  r1/a2:  0x000000ba  r2/a3:  0x00000000
> E: r3/a4:  0x20009ebd r12/ip:  0x00000000 r14/lr:  0x0000d51d
> E:  xpsr:  0x61000016
> E: s[ 0]:  0x00000000  s[ 1]:  0x00000000  s[ 2]:  0x00000000  s[ 3]:  0x00000000
> E: s[ 4]:  0x00000000  s[ 5]:  0x00000000  s[ 6]:  0x00000000  s[ 7]:  0x00000000
> E: s[ 8]:  0x00000000  s[ 9]:  0x00000000  s[10]:  0x00000000  s[11]:  0x00000000
> E: s[12]:  0x00000000  s[13]:  0x00000000  s[14]:  0x00000000  s[15]:  0x00000000
> E: fpscr:  0x00000000
> E: Faulting instruction address (r15/pc): 0x0004d5fe
> E: >>> ZEPHYR FATAL ERROR 4: Kernel panic on CPU 0
> E: Fault during interrupt handling
>


```c
static void button_pressed(const struct device *gpio_dev, struct gpio_callback *cb,
		    uint32_t pins)
{
	k_spinlock_key_t key = k_spin_lock(&lock);

	/* Disable GPIO interrupt */
	int err = callback_ctrl(false);

	if (err) {
		LOG_ERR("Cannot disable callbacks");
	}

	switch (state) {
	case STATE_WAITING:
		state = STATE_SCANNING;
		k_work_reschedule(&buttons_scan, K_MSEC(1));
		break;

	case STATE_SCANNING:
	default:
		/* Invalid state */
		__ASSERT_NO_MSG(false);
		break;
	}

	k_spin_unlock(&lock, key);
}

```