from redis.client import StrictRedis

if __name__ == '__main__':
    try:
        rs = StrictRedis(host='localhost', port=6379, db=0)

        # rs.hset('cart_1', 1, 2)
        # rs.hset('cart_1', 2, 3)
        # id1 = int(rs.hget('cart_1', 1).decode()) + 1
        # result = rs.hset('cart_1', 1, id1)
        rs.hmset('cart_2', {1: 2, 2: 3})
        # sum = 0
        # for count in rs.hvals('cart_1'):
        #    sum+= int(count.decode())
        # print(sum)
        result = rs.hdel('cart_1', 1)
        print(result)

    except Exception as e:
        print(e)
