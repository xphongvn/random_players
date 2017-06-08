import numpy as np

def random_combination(rank1, rank2, rank3):
    i = 0
    random_index = np.random.randint(0,5)
    first_combi = (rank1[0], rank2[random_index], rank3[0])
    print("Doi 1: {}".format(first_combi))

    number_left = 4

    rank1 = np.delete(rank1,0)
    rank2 = np.delete(rank2, random_index)
    rank3 = np.delete(rank3, 0)

    for i in xrange(1,5):
        random_index_rank1= np.random.randint(0,number_left)
        random_index_rank2 = np.random.randint(0, number_left)
        random_index_rank3 = np.random.randint(0, number_left)
        next_combi = (rank1[random_index_rank1], rank2[random_index_rank2],rank3[random_index_rank3])
        print("Doi {0}: {1}".format(i+1,next_combi))
        rank1 = np.delete(rank1, random_index_rank1)
        rank2 = np.delete(rank2, random_index_rank2)
        rank3 = np.delete(rank3, random_index_rank3)
        number_left -= 1


rank_1 = np.array(["LeDzung",
                   "Phan Hoang",
                   "Phan Huy",
                   "Nhat",
                   "Son Rose"])

rank_2 = np.array(["Duc Nguyen",
                   "Son Be",
                   "Manh Hoang",
                   "Hoang Tung",
                   "Tuan Anh"])

rank_3 = np.array(["Trang Nho",
                   "Bao Ngoc",
                   "Trung Hieu",
                   "Duc Hung",
                   "Ashley"])


random_combination(rank_1, rank_2, rank_3)