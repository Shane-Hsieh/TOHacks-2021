test_dict = {
    'aatrox_top':{"counters": "Aatrox top counters: https://na.op.gg/champion/aatrox/statistics/top/matchup",
                  "builds":"Aatrox top builds: https://na.op.gg/champion/aatrox/statistics/top/item",
                  "general":"Aatrox top general page: https://na.op.gg/champion/aatrox/statistics/top"},

    'aatrox_mid':{"counters": "Aatrox mid counters: https://na.op.gg/champion/aatrox/statistics/mid/matchup",
                  "builds":"Aatrox mid builds: https://na.op.gg/champion/aatrox/statistics/mid/item",
                  "general":"Aatrox mid general page: https://na.op.gg/champion/aatrox/statistics/mid"}

    'ahri_mid':{"counters": "https://na.op.gg/champion/ahri/statistics/mid/matchup",
                  "builds":"https://na.op.gg/champion/ahri/statistics/mid/item",
                  "general":"https://na.op.gg/champion/ahri/statistics/mid"}
}

print(type(test_dict))

print(test_dict['aatrox_top']['counters'])
print(test_dict['aatrox_top']['builds'])
print(test_dict['aatrox_top']['general'])
print("\n")
print(test_dict['aatrox_mid']['counters'])
print(test_dict['aatrox_mid']['builds'])
print(test_dict['aatrox_mid']['general'])
#print(test_dict["two"])

!aatrox_top_counters