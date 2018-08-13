"""
Sabermetrics Research
This file sets up the dynamic programming tables for an HMM model of MLB
pitching or pitch sequences, taking matchup data into account
Then uses a viterbi traceback algorithm to analyze effectiveness of specific
pitches and pitch sequences

Emily Barranca
Fall 2018
"""

#need to feed in data
#that is, pitcher's stats and opposing lineup and stats
#calculate liklihood of hit, extra base hit,
#for a batter, hidden states would be bitch and we'd have probabilities of
#emitting certain hits or swing/miss from each state --also probability of ball- come from pitcher

#changes through a lineup --
#maybe this can determine pitch sequences that would be effective against a batter
#then be run again with a pitcher and a pitch sequence in mind 
