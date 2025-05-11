from kafka import KafkaConsumer
import json
from channels.whatsappservice import WhatsAppService
from src.config import AppConfig

class KafkaConsumerService:
    def __init__(self, topic_name, kafka_server='localhost:9092', group_id='my-group'):
        # Initialize the KafkaConsumer to consume messages from the specified topic
        self.consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=kafka_server,  # Kafka broker address
            group_id=group_id,  # Consumer group ID
            auto_offset_reset='earliest',  # Start reading from the earliest messages
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))  # Deserialize the message from JSON format
        )

        # Create a WhatsAppService instance
        self.whatsapp_service = WhatsAppService()
        self.appConfig = AppConfig()

    def consume_messages(self):
        print("Listening for messages...")
        try:
            for message in self.consumer:
                # Print the consumed message
                message_value = message.value
                print(f"Consumed message value: {message_value['message']}")
                self.whatsapp_service.send_whatsapp_message(self.appConfig.twillio_recipient_whatsapp_number, message_value['message']['value'])
        except Exception as e:
            print(f"Failed to consume messages: {e}")
        finally:
            # Close the consumer connection when done
            self.consumer.close()

# Example usage
if __name__ == "__main__":
    # Create an instance of KafkaConsumerService
    kafka_consumer = KafkaConsumerService(topic_name='reactive-topic', kafka_server='localhost:9092')

    # Start consuming messages
    kafka_consumer.consume_messages()
