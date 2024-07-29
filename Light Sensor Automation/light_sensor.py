# create a program that reads the light sensor and automates the LED light
# it must work with Arduino and Python
# PIR sensor is used to detect motion and light sensor is used to detect light
# if the light sensor detects light, the LED light will turn off
# if the light sensor does not detect light, the LED light will turn on
# the PIR sensor will detect motion and turn on the LED light
# the LED light 'on' and 'off' State Transitioning conditions
# 1. if the light sensor detects light, the LED light will turn off/remain off
# 2. if the light sensor detects light, the PIR sensor ignored
# 3. if the light sensor does not detect light, the LED light will turn on/remain on, the PIR sensor ignored, the Timer will start countdown set by the user, the PIR sensor will be activated.
# 4. if the PIR sensor detects NO motion for the set time, the LED light will dim by 50% until the PIR sensor detects motion then the LED light will get brighter.
# 5. the LED light will stay on until the light sensor detects light, then the LED light will turn off and the PIR sensor will be ignored until the light sensor detects no light.
# 3. if the PIR sensor detects motion, the LED light will turn on
# 4. if the PIR sensor does not detect motion, the LED light will turn off
# 5. if the light sensor detects light and the PIR sensor detects motion, the LED light will turn off
# 6. if the light sensor does not detect light and the PIR sensor does not detect motion, the LED light will turn on
# 7. if the light sensor does not detect light and the PIR sensor detects motion, the LED light will turn on
# 8. if the light sensor detects light and the PIR sensor does not detect motion, the LED light will turn off