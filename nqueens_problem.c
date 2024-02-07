#include <stdio.h>

#define N 4

int total_ways = 0;

void printSolution(int board[N][N]) {
    printf("Arrangement #%d\n", ++total_ways);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", board[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int isSafe(int board[N][N], int row, int col) {
    // Check this row on the left side
    for (int i = 0; i < col; i++) {
        if (board[row][i] == 1) {
            return 0;
        }
    }

    // Check the upper diagonal on the left side
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1) {
            return 0;
        }
    }

    // Check the lower diagonal on the left side
    for (int i = row, j = col; i < N && j >= 0; i++, j--) {
        if (board[i][j] == 1) {
            return 0;
        }
    }

    return 1;
}

int solveNQUtil(int board[N][N], int col) {
    if (col >= N) {
        printSolution(board);
        return 1;
    }

    int res = 0;
    for (int i = 0; i < N; i++) {
        if (isSafe(board, i, col)) {
            board[i][col] = 1;
            res += solveNQUtil(board, col + 1);
            board[i][col] = 0;
        }
    }

    return res;
}

void solveNQ() {
    int board[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            board[i][j] = 0;
        }
    }

    int solutions = solveNQUtil(board, 0);

    if (solutions == 0) {
        printf("Solution does not exist\n");
    } else {
        printf("Total number of ways to arrange queens: %d\n", total_ways);
    }
}

int main() {
    solveNQ();
    return 0;
}
