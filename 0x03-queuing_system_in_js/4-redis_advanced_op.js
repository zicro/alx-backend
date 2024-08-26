import redis from "redis";

const client = redis.createClient()
    .on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
    .on('connect', () => console.log('Redis client connected to the server'));

client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);


client.hgetall('HolbertonSchools', (err, value) => {
    if (err) {
        console.error('error');
    } else {
        console.log(value);
    }
})
