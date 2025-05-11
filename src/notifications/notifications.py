from src.kafka_services.producerservice import KafkaProducerService

def publish(message:str, topic: str):
    
    kafka_service = KafkaProducerService()
    # Define the topic and message
    msg = {'key': 'value', 'message': message}

    # Call the method to send the message
    kafka_service.send_message(topic, msg)

    # Close the Kafka producer after usage
    kafka_service.close()