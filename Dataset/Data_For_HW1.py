import pandas as pd

PartyList = pd.read_excel('C:/Users/fifa-/OneDrive/KMUTT fibo/allpython/ML/Dataset/ECT.xlsx', sheet_name='result_constituencies_PartyList', header=0)
Candidate = pd.read_excel('C:/Users/fifa-/OneDrive/KMUTT fibo/allpython/ML/Dataset/ECT.xlsx', sheet_name='result_constituencies_Candidate', header=0, usecols=[0,2,3,4,5])
#print(Candidate.loc[0])
#print(PartyList.loc[0])
#print('Candidate = ',len(Candidate))
#print('PartyList = ',len(PartyList))

mp_app_rank = []
mp_app_vote = []
mp_app_vote_percent = []
for i in range(len(PartyList)):
    mp_app_rank.append(0)
    mp_app_vote.append(0)
    mp_app_vote_percent.append(0)

#print(len(mp_app_rank), len(mp_app_vote), len(mp_app_vote_percent))

for j in range(len(Candidate)):
    for i in range(len(PartyList)):
        if PartyList.loc[i][0] == Candidate.loc[j][0] and PartyList.loc[i][1] == Candidate.loc[j][4]:
            mp_app_rank[i] = Candidate.loc[j][1]
            mp_app_vote[i] = Candidate.loc[j][2]
            mp_app_vote_percent[i] = Candidate.loc[j][3]
            #print(PartyList.loc[i][0],Candidate.loc[j][0],PartyList.loc[i][1],Candidate.loc[j][4])
            break


All_result_constituencies = PartyList
All_result_constituencies['mp_app_rank'] = mp_app_rank
All_result_constituencies['mp_app_vote'] = mp_app_vote
All_result_constituencies['mp_app_vote_percent'] = mp_app_vote_percent
#print(All_result_constituencies)

All_result_constituencies.to_csv('C:/Users/fifa-/OneDrive/KMUTT fibo/allpython/ML/Dataset/All_result_constituencies.csv',index=False)