# Exc 9: Block or Not?
# Kevin Key
# 10/21/2025

def bot8(pbot, p8_bot, p8_human):
    """
    Return only the probability P(bot | 8-digits)
    """

    phuman = 1 - pbot
    p_8digits = (p8_bot * pbot) + (p8_human * phuman)    # P(8-digits)

    if p_8digits == 0:
        print("0")
        return

    pbot_given_8 = (p8_bot * pbot) / p_8digits   # P(bot | 8-digits)

    # Print only the probability
    print(pbot_given_8)

# Example imput values
pbot = 0.01
p8_bot = 0.8
p8_human = 0.05
bot8(pbot, p8_bot, p8_human)

