
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class HealthAnalyzer:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def get_summary_stats(self):
        columns = ["age", "weight", "height", "systolic_bp", "cholesterol"]
        stats = self.df[columns].agg(["count", "mean", "std", "median", "max", "min"])
        return stats

    def plot_bp_histogram(self):
        fig, ax = plt.subplots(figsize=(9, 4))
        ax.hist(
            self.df["systolic_bp"],
            bins=10,
            color="skyblue",
            edgecolor="black"
        )
        ax.set_title("Histogram över blodtryck")
        ax.set_xlabel("Systoliskt BP")
        ax.set_ylabel("Antal observationer")
        plt.tight_layout()
        plt.show()

    def plot_box_graph(self):
        fig, ax = plt.subplots(figsize=(7, 4))
        self.df.boxplot(column="weight", by="sex", ax=ax)
        ax.set_title("Weight per Gender")
        ax.set_xlabel("Gender")
        ax.set_ylabel("Weight")
        plt.suptitle("")
        plt.tight_layout()
        plt.show()

    def simulate_disease_probability(self, n_people=1000):
        
        real_prob = self.df["disease"].mean()
        real_percent = real_prob * 100

        simulated = np.random.binomial(n=1, p=real_prob, size=n_people)
        simulated_percent = simulated.mean() * 100

        print(f"{real_percent:.1f}% verkliga andelen personer har sjukdom.")
        print(f"{simulated_percent:.1f}% simulerade andelen personer har sjukdom.")

        return real_percent, simulated_percent
     
