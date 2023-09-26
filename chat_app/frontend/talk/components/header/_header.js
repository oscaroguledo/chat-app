import { Link, Stack } from 'expo-router';
import { Image, Text, View, Button } from 'react-native';
import Icon from '../icon/_icon';
import {COLORS, SHADOWS, SIZES} from "../../constants/theme";
import _headerBtn from "../header/_headerBtn";


function Header({title}) {

    return (
        <View >
            <Stack.Screen
                options={{
                // https://reactnavigation.org/docs/headers#setting-the-header-title
                title: {title},
                // https://reactnavigation.org/docs/headers#adjusting-header-styles
                headerStyle: { backgroundColor: COLORS.background },
                headerTintColor: '#fff',
                headerTitleStyle: {
                    fontWeight: 'bold',
                    color:COLORS.primaryText
                },
                headerShadowVisible: SHADOWS.small,
                headerLeft: () => (
                    <Text style={{padding:SIZES.xSmall}}>
                        <_headerBtn icon="contacts" />
                    </Text>
                ),
                
                headerRight: () => (
                    <Text style={{padding:SIZES.xSmall}}>
                        <_headerBtn icon="search1" style={{padding:10}}/>
                        <_headerBtn icon="setting" />
                    </Text>
                    
                ),
                
                // https://reactnavigation.org/docs/headers#replacing-the-title-with-a-custom-component
                headerTitle: title,
                headerTitleAlign:'center',
                horizontal:true,
                

                }}
            />
        </View>
      
    );
  }
  
export default Header;
  