"""
______________________________________________________________________________
⌘ -·-·-·-·-·-·-·-·-·-·-  An Ode to Lovelace's Note G -·-·-·-·-·-·-·-·-·-·- ⌘
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
About:  In honour of Ada Lovelace, and the worlds first computer program which
        Lovelace wrote, which can be found in a collection of Lovelaces notes 
        on a note labelled G. Her code was written to calculate Bernouilli 
        numbers. This program calculates Bernouilli numbers using the recursive
        method, which is Lovelace was using.

        Note G was the last of a series of notes written by Lovelace which
        she had added to an English translation of Charles Babbage's lectures,
        which Babbage had given in Turin in 1842. Lovelace's notes, along with
        her translation, were published in 1843. Note G contains the first 
        ever code written for a computer.

        The program was never run as the machine that it was written for, 
        the analytic engine, was never built. Note G also contained the
        first ever bug as one division was the wrong way around.

        Lovelace's original program was written to calculate the 8th
        Bernoulli number -1/30 ≈ 0.033333333 but due to the small error
        would have returned  -25621/630 ≈ -40.6682539683.

        This program, thanks to being able to run and test my code, a 
        luxury not available to Lovelace, *should* return Bernouilli
        numbers, albeit within the limits of a finte precision
        computer.

        This program is written for fun only. For faster and more stable 
        calculation of Bernoulli numbers in Python, 
        use scipy.special bernoulli

        For more info:
        https://en.wikipedia.org/wiki/Ada_Lovelace
        https://en.wikipedia.org/wiki/Note_G
        https://en.wikipedia.org/wiki/Bernoulli_number
______________________________________________________________________________
⌘ -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-· ⌘
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
."""

from math import factorial as fac
import decimal as dec

# to determine the precision of the numbers. 
dec.getcontext().prec = 20

def bern(m):
    """
    A recursive function to calculate the m_th Bernoulli number
    Inputs:     int m
    Return:     Decimal - the mth Bernoulli number or False in the event of input
                error.
    ."""
    if not isinstance(m, int):
        print("ERROR: please enter an positie integer.")
        return False
    elif m < 0:
        print("ERROR: please enter an positie integer.")
    else:
        if m > 0:
            return dec.Decimal(1-sum([fac(m)*bern(k)/(fac(k)*fac(m-k+1)) for k in range(0,m)]))
        else:
            return dec.Decimal(1)
        
print("\n".join([f"{n}  {bern(n)}" for n in range(0, 20)]))

input_number = int(input("please enter a number\n"))
print(f"The {input_number}th Bernouilli number = {bern(input_number)}")    



