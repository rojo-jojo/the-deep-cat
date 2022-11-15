#include <stdio.h>
#include <gsl/gsl_math.h>

double sigmoid(double x)
{
    return 1/(1 + exp(-x));
}

void log_reg(double* w1, double* w2, double* b)
{
    double J = 0, dw1 = 0, dw2 = 0,db = 0;
    const int m = 100; //Size of training data
    double z[m], a[m];
    double x[2][m];
    double y[m];
    double lr = 0.001;
    for (int i=0; i<m; i++)
    {
        //Forward pass
        z[i] = *w1 * x[0][i] + *w2 * x[1][i] + *b;
        a[i] = sigmoid(z[i]);
        J += (y[i] * log(a[i]) + (1-y[i]) * log(1-a[i]));

        //Backward pass
        double dz_i = a[i] - y[i];
        dw1 += dz_i * x[0][i];
        dw2 += dz_i * x[1][i];
        db += dz_i;
    }
    J /= m;
    dw1 /= m;
    dw2 /= m;
    db /= m;
    // Gradient descent
    *w1 = *w1 - lr * dw1;
    *w2 = *w2 - lr * dw2;
    *b = *b - lr * db;

}

void main() {
    int epochs = 10;
    for (int i=0; i<epochs; i++)
    {
        
    }
}