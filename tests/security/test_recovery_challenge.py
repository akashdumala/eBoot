from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECOVERY_SOURCE = ROOT / "core" / "recovery.c"


def test_recovery_challenge_fails_closed_without_rng():
    """Recovery must never replace a failed CSPRNG with a predictable seed."""
    source = RECOVERY_SOURCE.read_text(encoding="utf-8")

    assert "eos_hal_rng_get(challenge, RCVR_CHALLENGE_SIZE)" in source
    assert "Fallback: use tick-based pseudo-random" not in source
    assert "Never fall back to a predictable challenge source." in source
    assert "return recovery_send_nack();" in source
