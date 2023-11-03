import { Tabs } from 'expo-router';
import React, {useRef, useEffect} from 'react';
import {Animated, Text, View} from 'react-native';
import {Icon,Icon2 }from '../components/icon/_icon';
import {Contact,Search,Setting} from '../components/header/_headerIcons';
import { COLORS, SHADOWS, SIZES } from '../constants/theme';
import Posts from "./post";

function Layout() {
  return (
    <Tabs screenOptions={{tabBarShowLabel:false}}>
        <Tabs.Screen name='index' options={
            {
                title: "Chats",
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
                        <Contact/>
                    </Text>
                ),
                
                headerRight: () => (
                    <Text style={{padding:SIZES.xSmall}}>
                        <Search/>
                        <Setting/>
                    </Text>   
                ), 
                // https://reactnavigation.org/docs/headers#replacing-the-title-with-a-custom-component
                headerTitle: "Chats",
                headerTitleAlign:'center',
                horizontal:true,
                headerShown: false,
                tabBarIcon:({icon}) =>(
                    <Icon icon={'message1'} />
                )
            }
        } />
        <Tabs.Screen name='phone' options={
            {
                tabBarIcon:({icon}) =>(
                    <Icon icon={'phone'} />
                )
            }
        } />
        
        <Tabs.Screen name='groups' options={
            {
                tabBarIcon:({icon}) =>(
                    <Icon2 icon={'users'}  />
                )
            }
        } />
        <Tabs.Screen name='post' options={
            {
                tabBarIcon:({icon}) =>(
                    <Icon icon={'antdesign'} />
                )
            }
        } />
        <Tabs.Screen name='profile' options={
            {
                tabBarIcon:({icon}) =>(
                    <Icon2 icon={'user'} />
                )
            }
        } />
    </Tabs>
  );
}

export default Layout;
