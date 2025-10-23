import numpy as np

def kalman_filter(signal, process_var=1e-2, measurement_var=1):
    """
    Apply a simple Kalman filter for 1D time series denoising.

    Parameters:
    - signal: The noisy time series data.
    - process_var: Process variance (smaller values result in smoother filtering).
    - measurement_var: Measurement variance (higher values assume more noise in observations).
s
    Returns:
    - filtered_signal: The estimated clean time series.
    """

    n = len(signal)
    filtered_signal = np.zeros(n)
    uncertainty = 1.0  # Initial guess for state uncertainty
    estimate = signal[0]  # Initial state estimate

    for t in range(n):
        # Prediction step
        estimate = estimate  # State transition (identity model)
        uncertainty += process_var  # Increase uncertainty

        # Update step
        kalman_gain = uncertainty / (uncertainty + measurement_var)
        estimate = estimate + kalman_gain * (signal[t] - estimate)
        uncertainty = (1 - kalman_gain) * uncertainty

        filtered_signal[t] = estimate

    return filtered_signal