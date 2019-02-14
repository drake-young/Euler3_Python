from timeit import default_timer


# ===========================================================
# FUNCTION: get_largest_prime_factor
# ===========================================================
#
#  Input: integer n to find the largest prime factor of
#
#  Output: the largest prime number that divides n
#
#  Task:    iterate through integers <= sqrt(n), checking if
#           that integer divides n. this continues until all
#           integers that divide n have been accounted for,
#           and returns that integer
#
# ===========================================================
def get_largest_prime_factor( n ):
    # Variables
    i        =  2
    largest  =  0

    # Check integers between 2 and sqrt(n)
    while i * i <= n:

        # If the current integer divides n, divide n (factor i out)
        if n % i is 0:
            n      //=  i
            largest  =  i

        # If the integer does not divide n, then increment and continue
        else:
            i  +=  1

    # Return the largest factor (or n if n was prime)
    return max( largest , n )



# ===========================================================
# PROBLEM 3 -- Largest prime factor
# ===========================================================
#
# The prime factors of 13195 are 5, 7, 13, and 29
#
# What is the largest prime factor of the number 600851475143
#
# ===========================================================
def problem_3( n=600851475143 ):
    # Display the Problem Context
    print( "Project Euler Problem 3 -- Largest Prime Factor")

    # Prepare Variables
    start_time      =  default_timer( )
    result          =  get_largest_prime_factor( n )
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   Largest prime factor of the number %d:   %d"                %  ( n , result ) )
    print( "   Computation Time:                                  %.3fms"  %  execution_time )
    return



if __name__ == '__main__':
    problem_3( )
