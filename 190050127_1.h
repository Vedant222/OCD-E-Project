#include <algorithm>
#include <iostream>

class permutation {
public:
    int p[100];
    int n_arr;
    permutation(int n, int a[]) {
        for (int i = 0; i < n; i++) {
            p[i] = a[i];
        }
        n_arr = n;
    }

    ~permutation() = default;

    permutation (permutation const &q) {
        n_arr = q.n_arr;
        for (int i = 0; i < n_arr; i++) {
            p[i] = q.p[i];
        }
    }

    permutation const operator= (permutation const &q) {
        n_arr = q.n_arr;
        for (int i = 0; i < n_arr; i++) {
            p[i] = q.p[i];
        }
        return *this; 
    }

    int size() const {
        return n_arr;
    }

    int* to_array () const {
        int *arr = new int[n_arr];
        for (int i = 0; i < n_arr; i++) {
            arr[i] = p[i];
        }
        return arr;
    }

    permutation const operator- () const {
        int arr[100];
        int n = n_arr;
        

        for(int i = 0; i < n; i++){
             arr[p[i]] = i;
        }

        return permutation(n, arr);
    }



    permutation const operator*(permutation const &q) const{
        int arr[100];
        int n = n_arr;

        for (int i = 0; i < n; i++) {
            arr[i] = p[q.p[i]];
        }

       return permutation(n, arr);       
    }

    permutation const operator^(long long int power) const{
        int arr[100];
        int n = n_arr;
        for (int i = 0; i < n_arr; i++) {
            arr[i] = i;
        }
        permutation res(n, arr);

        for (long long int i = 0; i < power; i++) {
            res = res * (*this);
        }
        return res;
    } 

    bool operator== (permutation const& q) const {
        for (int i = 0; i < n_arr; i++) {
            if (p[i] != q.p[i]) return false;
        }
        return true;
    }

    bool is_power (permutation const &q) {
        permutation q_temp(q);
        for (long long int i = 0; i < 1e18; i++) {
            if ((*this) == q_temp) return true;
            q_temp = q_temp * q;
        }
        return false;
    }

    permutation const square_root () const{
        int a[100];
        for (int i = 0; i < n_arr; i++) a[i] = i;
        while (std::next_permutation(a, a + n_arr)) {
            permutation test(n_arr, a);
            if (test == (*this)) return test; 
        }
        for (int i = 0; i < n_arr; i++) a[i] = i;
        return permutation(n_arr, a);
    }

    int log (permutation const &q) {
        permutation q_temp(q);
        for (long long int i = 0; i < 1e18; i++) {
            if ((*this) == q_temp) return i % 1000000007;
            q_temp = q_temp * q;
        }
        return 0;
    }

};
