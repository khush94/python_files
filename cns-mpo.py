class CNS_MPO_Score:
    def __init__(self, clogP, clogD, cTPSA, cMW, cHBD, cpKa):
        self.clogP = clogP
        self.clogD = clogD
        self.cTPSA = cTPSA
        self.cMW = cMW
        self.cHBD = cHBD
        self.cpKa = cpKa
    def clogPCalculation(self):
        logP = 0
        if self.clogP <= 3:
            return 1
        elif 3 < self.clogP < 5:
            logP += 1 - (self.clogP - 3)/2
            return logP
        else:
            return 0
    def clogDCalculation(self):
        logD = 0
        if self.clogD <= 2:
            return 1
        elif 2 < self.clogD < 4:
            logD += 1 - (self.clogD - 2)/2
            return logD
        else:
            return 0
    def TPSACalculation(self):
        TPSA = 0
        if 40 <= self.cTPSA <= 90:
            return 1

        elif 20 < slef.cTPSA < 40:
            TPSA += (self.cTPSA - 20)/20
            return TPSA

        elif 90 < self.cTPSA < 120:
            TPSA += 1 -(self.cTPSA - 90)/30
            return TPSA
        else:
            return 0
    def MWCalculation(self):
        MW = 0
        if self.cMW <= 360:
            return 1
        elif 360 < self.cMW < 500:
            MW += 1 - (self.cMW - 360)/140
            return MW
        else:
            return 0
    def HBDCalculation(self):
        HBD = 0
        if self.cHBD == 0:
            return 1
        elif 0.5 < self.cHBD < 3.5:
            HBD += 1 - (self.cHBD - 0.5)/3
            return HBD
        else:
            return 0
    def clogpKa(self):
        pKa = 0
        if self.cpKa <= 8:
            return 1
        elif 8 < self.cpKa < 10:
            pKa += 1 - (self.cpKa - 8)/2
            return pKa
        else:
            return 0
    def get_cns_mpo_score(self):
        cns_score = 0
        cns_score = self.logP + self.logD + self.TPSA + self.MW + self.HBD + self.pKa
        return cns_score



cns = CNS_MPO_Score(3.20, 2.48, 79, 407, 4, 3)

print(cns.get_cns_mpo_score())
