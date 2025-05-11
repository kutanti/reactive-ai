from kafka import KafkaProducer
import json

class KafkaProducerService:
    def __init__(self, kafka_server='localhost:9092'):
        """
        Initializes the KafkaProducer instance.

        :param kafka_server: The Kafka broker address (default is 'localhost:9092').
        """
        # Initialize the KafkaProducer when the class is instantiated
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_server,  # Kafka broker address
            value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize message to JSON format
        )

    def send_message(self, topic_name, message):
        """
        Sends a message to the specified Kafka topic.

        :param topic_name: The name of the Kafka topic.
        :param message: The message to be sent (should be serializable to JSON).
        """
        try:
            # Send the message to the specified Kafka topic
            self.producer.send(topic_name, value=message)

            # Ensure all messages are sent before returning
            self.producer.flush()

            print(f"Message sent to topic '{topic_name}' successfully.")
        except Exception as e:
            print(f"Failed to send message to topic '{topic_name}': {e}")

    def close(self):
        """
        Closes the KafkaProducer instance.
        """
        self.producer.close()

# Example usage
if __name__ == "__main__":
    # Create an instance of KafkaProducerService
    kafka_service = KafkaProducerService(kafka_server='localhost:9092')

    # Define the topic and message
    topic = 'reactive-topic'
    msg = {'key': 'value', 'message': 'Hello, your HDFCBANK stock will explode, From, Allyce!'}

    # Call the method to send the message
    kafka_service.send_message(topic, msg)

    # Close the Kafka producer after usage
    kafka_service.close()
