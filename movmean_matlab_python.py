import numpy as np



def shrink_bc(fcn, x, idxp, win, wlen, odim=1):
    N = len(x)
    idx = idxp + win.reshape(len(win),1)
    tf = (idx > 0) & (idx <= N)

    n = len(idxp)
    y = np.zeros((n))
    
    for i in range(n):
        k = idx[tf[:, i], i]
        y[i] = fcn(x[k-1])
    
    return y



def movslice(N, wlen):
    
    # Calculate nb and na
    if isinstance(wlen, int):
        if wlen % 2 == 1:
            nb = na = (wlen - 1) // 2
            wlen = [nb, na]
        else:
            nb = wlen // 2
            na = nb - 1
            wlen = [nb, na]

    Cpre = np.arange(1, wlen[0] + 1)
    Cnf = N - wlen[1] + 1
    Cpost = np.arange(Cnf, N + 1)
    C = np.arange(wlen[0] + 1, Cnf)
    win = np.arange(-wlen[0], wlen[1] + 1)
    slcidx = C + win.reshape(len(win),1)

    return slcidx, C, Cpre, Cpost, win







def movmean(amp, window):
    N = len(amp)
    y2 = np.convolve(amp, np.ones(window) / window, mode='valid')
    slcidx, C, Cpre, Cpost, win = movslice(N, window)
    fcn = np.mean
    y1 = shrink_bc(fcn, amp, Cpre, win, window)
    y3 = shrink_bc(fcn, amp, Cpost, win, window)
    return np.array(y1.tolist()+y2.tolist()+y3.tolist())

# Example usage:
amp = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12])
window = 5

moving_average = movmean(amp, window)
print(moving_average)






