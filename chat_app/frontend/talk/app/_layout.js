import { Tabs } from 'expo-router';
import React, {useRef, useEffect} from 'react';
import {Animated, Text, View} from 'react-native';
import {Icon,Icon2 }from '../components/icon/_icon';

function Layout() {
  return (
    <Tabs screenOptions={{tabBarShowLabel:false}}>
        <Tabs.Screen name='phone' options={
            {
                tabBarIcon:({icon}) =>(
                    <Icon icon={'phone'} />
                )
            }
        } />
        <Tabs.Screen name='chats' options={
            {
                tabBarIcon:({icon}) =>(
                    <Icon icon={'message1'} />
                )
            }
        } />
        <Tabs.Screen name='index' options={
            {
                tabBarIcon:({icon}) =>(
                    <Icon icon={'camerao'}  />
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
        <Tabs.Screen name='options' options={
            {
                tabBarIcon:({icon}) =>(
                    <Icon icon={'ellipsis1'} />
                )
            }
        } />
    </Tabs>
  );
}

export default Layout;
