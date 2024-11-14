class ImprovabilityScore:
    def __init__(self, table):
        self.table = table
    
    def assign_support_level(self, data):
        support_mapping = {cluster: score for score, cluster in enumerate(self.table.index, start=1)}
        data['Improvability_score'] = data['cluster'].map(support_mapping)
        return data
            
