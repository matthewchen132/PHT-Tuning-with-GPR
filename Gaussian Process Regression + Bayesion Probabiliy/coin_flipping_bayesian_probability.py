import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
 
# Using Bayesian principles, we can derive statistical probabilities
# for noisy, unpredictable systems through exepriment. -> could be used for sensor characterizing
if __name__ == "__main__":
    # Create a list of the number of coin tosses ("Bernoulli trials")
    number_of_tosses = 50

    # Conduct 500 coin tosses and output into a list of 0s and 1s
    # where 0 represents a tail and 1 represents a head
    data = stats.bernoulli.rvs(0.5, size=number_of_tosses)
    print(data)
    
    # Discretise the x-axis into 100 separate plotting points
    x = np.linspace(0, 1, 100)
    
    # Loops over the number_of_trials list to continually add
    # more coin toss data. For each new set of data, we update
    # our (current) prior belief to be a new posterior. This is
    # carried out using what is known as the Beta-Binomial model.
    # For the time being, we won't worry about this too much. It 
    # will be the subject of a later article!
        # Accumulate the total number of heads for this 
        # particular Bayesian update
    heads = data.sum()
    # Create an axes subplot for each update 
    ax = plt.subplot(1, 2, 1)
    ax.set_title("%s trials, %s heads" % (number_of_tosses, heads))

    # Add labels to both axes and hide labels on y-axis
    plt.xlabel("$P(H)$, Probability of Heads")
    plt.ylabel("Density")
    plt.setp(ax.get_yticklabels(), visible=False)
                
    # Create and plot a  Beta distribution to represent the 
    # posterior belief in fairness of the coin.
    y = stats.beta.pdf(x, 1 + heads, 1 + number_of_tosses - heads)
    plt.plot(x, y, label="observe %d tosses,\n %d heads" % (number_of_tosses, heads))
    plt.fill_between(x, 0, y, color="#aaaadd", alpha=0.5)

    # Expand plot to cover full width/height and show it
    plt.tight_layout()
    plt.show()