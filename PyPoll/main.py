import pandas as pd
import numpy as np

#Calculate Total Number of Votes

election_data = pd.read_csv("/Users/Jorda/Desktop/Python Homework/PyPoll/Resources/election_data.csv")

totalvotecount = len(election_data)
candidatecount = election_data["Candidate"]

candidatelist = list(set(candidatecount))
candidategroups = election_data.groupby(["Candidate"], group_keys=True)

#Calculate Total Candidate Vote Count 

candidatevotecounts = candidategroups.agg(["count"])["County"]["count"]

#Calculate Total Percentage Candiate Votes

correyvotes = ["Correy", round((candidatevotecounts["Correy"]/totalvotecount) * 100, 3), candidatevotecounts["Correy"]]

otooleyvotes = ["O'Tooley", round((candidatevotecounts["O'Tooley"]/totalvotecount) * 100, 3), candidatevotecounts["O'Tooley"]]

khanvotes = ["Khan", round((candidatevotecounts["Khan"]/totalvotecount) * 100, 3), candidatevotecounts["Khan"]]

livotes = ["Li", round((candidatevotecounts["Li"]/totalvotecount) * 100, 3), candidatevotecounts["Li"]]

winner = max([correyvotes, otooleyvotes, khanvotes, livotes], key=lambda x: x[1])

electionresults = ["Election Results",
"-------------------------",
"Total Votes:" + str(totalvotecount),
"-------------------------",
"Khan: " + '{}% ({})'.format(khanvotes[1], khanvotes[2]),
"Correy: " + '{}% ({})'.format(correyvotes[1], correyvotes[2]),
"Li: " + '{}% ({})'.format(livotes[1], livotes[2]),
"O'Tooley: " + '{}% ({})'.format(otooleyvotes[1], otooleyvotes[2]),
"-------------------------",
"Winner: " + str(winner[0]),
"-------------------------"]

with open("C:/Users/Jorda/Desktop/Python Homework/PyPoll/Analysis/analysis.txt", "w") as output:
    output.write(str(electionresults)+ "\n")

