import redis from "redis";

const client = redis.createClient();

client.on('error', (err) => { 
    console.log(`Redis client not connected to the server: ${err}`)
});

client.on('connect', () => {
    console.log('Redis client connected to the server')
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.log(`Error setting value: ${err}`);
        } else {
            redis.print('Replay: OK');
        }
    });
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, value) => {
        if (err) {
            console.log(`Error value: ${err}`);
        } else {
            console.log(value);
        }
    });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
