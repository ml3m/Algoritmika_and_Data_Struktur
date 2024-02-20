#include "comb_sort.h"
void comb_sort(char* s, int sz, tpifpcii order_is_broken, tpifpcii swap_items)
{
    int i, dif;
    const double factor = 1.2473309;

    dif = sz;
    while (dif >= 1)
    {
        for (i=0; i+dif < sz; i++)
        {
            if (order_is_broken(s, i, i+dif))
                swap_items(s, i, i+dif);
        }
        dif /= factor;
    }
}
