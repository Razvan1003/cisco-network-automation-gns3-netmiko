from __future__ import annotations

import configure_r1
import configure_r3
import configure_sw1


def main() -> None:
    print("Configuring SW1...")
    configure_sw1.main()
    print("Configuring R1...")
    configure_r1.main()
    print("Configuring R3...")
    configure_r3.main()


if __name__ == "__main__":
    main()
