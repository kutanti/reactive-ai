from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

# Initialize the KafkaAdminClient
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",  # Replace with your Kafka broker address
    client_id='my-client'
)

# Define the topic you want to create
topic_name = "reactive-topic"
num_partitions = 1
replication_factor = 1

# Create a NewTopic object
new_topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)

# Create the topic using KafkaAdminClient
try:
    admin_client.create_topics(new_topics=[new_topic], validate_only=False)
except TopicAlreadyExistsError:
    print(f"Topic '{topic_name}' already exists.")
except Exception as e:
    print(f"Failed to create topic '{topic_name}': {e}")
    print(f"Failed to create topic '{topic_name}': {e}")
finally:
    # Close the admin client
    admin_client.close()
