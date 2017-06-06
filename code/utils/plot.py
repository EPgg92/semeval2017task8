import json
import matplotlib.pyplot as plt


def by_epoch(epochs, loss, acc, time):
    plt.figure(1)
    plt.subplot(221)
    plt.title('Loss by Epochs')
    plt.plot(epochs, loss, 'r')
    plt.subplot(212)
    plt.title('Accuracy by Epochs')
    plt.plot(epochs, acc, 'r')
    plt.subplot(222)
    plt.title('Time by Epochs')
    plt.plot(epochs, time, 'r')
    plt.show()


def main():
    with open('steps.json', 'r') as stream:
        features = json.load(stream)
    loss, acc, time, epochs = [], [], [], []
    for w, x, y, z in features:
        loss.append(w)
        acc.append(x)
        time.append(y)
        epochs.append(z)
    by_epoch(epochs, loss, acc, time)


if __name__ == '__main__':
    main()
