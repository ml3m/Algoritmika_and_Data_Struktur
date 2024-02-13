#include <stdio.h>

// Problem 1
int calculate_S1(int m) {
    int result = 0;
    for (int i = 0; i <= m; i++) {
        result += i + (i * i);
    }
    return result;
}

int calculate_S1_recursive(int m) {
    if (m == 0)
        return 0;
    else
        return m + m * m + calculate_S1_recursive(m - 1);
}

// Problem 2
int calculate_S2(int m, int n) {
    int S2 = 0;
    for (int i = 1; i <= m; i++) {
        for (int j = i; j <= n; j++) {
            S2 += j + i;
        }
    }
    return S2;
}

// Problem 3
float calculate_S3(int m, int n) {
    float S3 = 0.0;
    for (int i = 1; i <= m; i++) {
        for (int j = i; j <= n; j++) {
            S3 += (float)j / i;
        }
    }
    return S3;
}

// Problem 4 (Trapezoidal Rule)
float f(float x) {
    return x * x;
}

float trapezoidal_rule(float (*func)(float), float a, float b, int n) {
    float h = (b - a) / n;
    float result = (func(a) + func(b)) / 2.0;

    for (int i = 1; i < n; i++) {
        result += func(a + i * h);
    }

    result *= h;
    return result;
}

int main() {
    int m_value = 5;
    int n_value_s2 = 4;
    int n_value_s3 = 4;

    printf("Problem 1: S1(%d) = %d\n", m_value, calculate_S1(m_value));
    printf("Problem 1 (Recursive): S1(%d) = %d\n", m_value, calculate_S1_recursive(m_value));
    printf("Problem 2: S2(%d, %d) = %d\n", m_value, n_value_s2, calculate_S2(m_value, n_value_s2));
    printf("Problem 3: S3(%d, %d) = %f\n", m_value, n_value_s3, calculate_S3(m_value, n_value_s3));

    // Problem 4 (Trapezoidal Rule)
    float a_value = 0.0;
    float b_value = 2.0;
    int n_value_trapezoidal = 100;

    float result_trapezoidal = trapezoidal_rule(f, a_value, b_value, n_value_trapezoidal);
    printf("The approximate integral using the Trapezoidal Rule is: %.4f\n", result_trapezoidal);

    return 0;
}
