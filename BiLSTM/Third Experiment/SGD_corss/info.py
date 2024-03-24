# EX 1
optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)
criterion = nn.CrossEntropyLoss()

cm = [[   0    0    0    6    1    0    0    0    0    0    0    0    0  604]
 [   0    0    0    0    0    0    0    0    0    0    0    0    0   89]
 [   0    0    0    0    0    0    0    0    0    0    0    0    0   88]
 [   0    0    0   10    6    0    0    0    0    0    0    0    0  850]
 [   0    0    0    5   71    0    0    0    0    0    0    0    0  763]
 [   0    0    0    3    0    0    0    0    0    0    0    0    0   21]
 [   0    0    0    6    1    0    0    0    0    0    0    0    0  431]
 [   0    0    0    3    0    0    0    0    0    0    0    0    0  343]
 [   0    0    0    2    4    0    0    0    0    0    0    0    0  228]
 [   0    0    0    1    1    0    0    0    0    0    0    0    0  175]
 [   0    0    0    1    1    0    0    0    0    0    0    0    0   48]
 [   0    0    0    3    1    0    0    0    0    0    0    0    0  108]
 [   0    0    0    2    3    0    0    0    0    0    0    0    0  285]
 [   0    0    0    8    3    0    0    0    0    0    0    0    0 1564]]

AUC = {0: 0.5574457552770196, 1: 0.47597892015511584, 2: 0.5236301700423095, 3: 0.5768795298977398, 4: 0.6325173311279219, 5: 0.5357830271216097, 6: 0.5814307458143075, 7: 0.5957262089906741, 8: 0.5979040033535946, 9: 0.5839473668172039, 10: 0.556547723677272, 11: 0.6865360570209957, 12: 0.6460508413438721, 13: 0.6002317673787414}
