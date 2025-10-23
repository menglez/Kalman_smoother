import matplotlib.pyplot as plt

def ploter(df, stock):
    # Create figure and three subplots with equal height ratios
    fig, (ax1, ax2, ax3) = plt.subplots(
        3, 1, figsize=(20, 10), sharex=True, gridspec_kw={'height_ratios': [1, 1, 1]}
    )

    # 1️⃣ Stock plot
    ax1.plot(df.index, df[stock], label=stock, color='blue')
    ax1.legend(loc='upper left')
    ax1.grid(True)
    ax1.set_title(f'{stock} and Kalman Filter Comparison')

    # 2️⃣ Kalman filter plot
    ax2.plot(df.index, df['kf'], label='kf', color='orange')
    ax2.legend(loc='upper left')
    ax2.grid(True)

    # 3️⃣ Combined plot
    ax3.plot(df.index, df[stock], label=stock, color='blue')
    ax3.plot(df.index, df['kf'], label='kf', color='orange')
    ax3.legend(loc='upper left')
    ax3.grid(True)
    ax3.set_xlabel('Date')

    plt.tight_layout()
    plt.show()
