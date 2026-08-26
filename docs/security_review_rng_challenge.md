# Recovery challenge RNG review

Recovery authentication must not fall back to a predictable challenge when the hardware RNG fails. A time-seeded pseudo-random challenge can be predictable and weakens the challenge-response protocol.

The recovery path should fail closed when the hardware RNG is unavailable.
