INSERT INTO OLD_OFFENSE(NAME, TEAM, POSITION, PASS_YARDS, PASS_TD, INTERCEPTIONS, RUSH_YARDS, RUSH_TD, REC_YARDS, REC_TD, FUM_TD, TWO_PT, FUM_LOST) SELECT * FROM CSVREAD('src/main/resources/player_stats_2017_2018.csv');
INSERT INTO OLD_KICKER(NAME, TEAM, PAT, TEENS, TWENTIES, THIRTIES, FORTIES, FIFTIES) SELECT * FROM CSVREAD('src/main/resources/k_stats_2017_2018.csv');
INSERT INTO OLD_DEFENSE(NAME, SACK, INTERCEPTIONS, FUM_REC, SAFETIES, TD, TWO_PT_RETURN, RET_TD, PTS_ALLOW) SELECT * FROM CSVREAD('src/main/resources/def_stats_2017_2018.csv');