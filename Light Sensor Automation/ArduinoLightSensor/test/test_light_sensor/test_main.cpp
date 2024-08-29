#include <Arduino.h>
#include <unity.h>

// Function prototypes
void test_led_on_when_dark_and_pir_triggered();
void test_led_off_when_light_or_pir_not_triggered();

void setup() {
    UNITY_BEGIN();    // Start Unity test framework

    // Run tests
    RUN_TEST(test_led_on_when_dark_and_pir_triggered);
    RUN_TEST(test_led_off_when_light_or_pir_not_triggered);

    UNITY_END();      // End Unity test framework
}

void loop() {
    // Empty loop
}

void test_led_on_when_dark_and_pir_triggered() {
    // Simulate PIR triggered and dark environment
    pinMode(2, INPUT);
    pinMode(A0, INPUT);
    pinMode(13, OUTPUT);

    digitalWrite(2, HIGH);
    analogWrite(A0, 400);

    // Call the loop function to test the behavior
    loop();

    // Check if LED is on
    TEST_ASSERT_EQUAL(HIGH, digitalRead(13));
}

void test_led_off_when_light_or_pir_not_triggered() {
    // Simulate PIR not triggered or light environment
    pinMode(2, INPUT);
    pinMode(A0, INPUT);
    pinMode(13, OUTPUT);

    digitalWrite(2, LOW);
    analogWrite(A0, 600);

    // Call the loop function to test the behavior
    loop();

    // Check if LED is off
    TEST_ASSERT_EQUAL(LOW, digitalRead(13));
}

