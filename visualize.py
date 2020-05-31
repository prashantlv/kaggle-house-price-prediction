
def visualize(data):

    import matplotlib.pyplot as plt 
    import seaborn as sns 

    print("Visualizing...")
    sns.heatmap(data.isnull())
    plt.show()