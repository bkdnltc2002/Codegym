america = data.loc[data["Continent"] == "America"]
print(stats.ttest_ind(europe["GDP (millions of US$)"],
      america["GDP (millions of US$)"], equal_var=True))