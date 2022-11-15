#include <stdio.h>
#include <math.h>
#include <gsl/gsl_math.h>
#include <gsl/gsl_deriv.h>

double f (double x, void * params)
{
    (void)(params); /*avoid unused parameter warning*/
    return pow (x, 1.5);
}

int main(void)
{
    gsl_function F;
    double result, abserr;

    F.function = &f;
    F.params = 0;
    printf ("f(x) = x^(3/2)\n");

    gsl_deriv_central(&F, 2.0, 1e-8, &result, &abserr);
    printf ("x = 2.0\n");
    printf ("f'(x) = %.10f +/- %.10f\n", result, abserr);

}