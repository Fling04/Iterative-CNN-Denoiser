import numpy as np

# Parameters
eta = 0.8
N = 576

# Generate covariance matrix
cov = np.zeros((N, N), dtype=np.float32)
for ii in range(N):
    for jj in range(ii, N):
        cov[ii, jj] = eta ** abs(ii - jj)
        cov[jj, ii] = cov[ii, jj]  # symmetric

# Compute the matrix square root
transfer_mat = np.linalg.cholesky(cov)
filename = f'cov_1_2_corr_para{eta:.2f}.dat'
transfer_mat.astype('float32').tofile(filename)
print(f"Matrix saved to {filename}")