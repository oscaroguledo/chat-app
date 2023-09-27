import React,{ useState } from 'react';
import { NavigationContainer, StackActions } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Image, SafeAreaView, FlatList, StyleSheet, Text, View, Button} from 'react-native';
import Header from '../components/header/_header';
import _headerBtn  from '../components/header/_headerBtn';
import {Contact,Search,Setting, Phone, Video} from '../components/header/_headerIcons';
import {ItemSeparator, Item} from "../components/List/List_Item";
import { COLORS, SIZES, SHADOWS } from '../constants/theme';
import {Chats, UserChat} from '../components/chat/chat';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer independent={true}>
      <Stack.Navigator >
        <Stack.Screen name="Chats" options={{
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
          horizontal:true
        }} 
        component={Chats} />

        <Stack.Screen name="UserChat" options={
          ({route}) =>(
            {
              // https://reactnavigation.org/docs/headers#adjusting-header-styles
              headerStyle: { backgroundColor: COLORS.background },
              headerTintColor: COLORS.primaryText,
              headerTitleStyle: {
                  fontWeight: 'bold',
                  color:COLORS.primaryText
              },
              headerShadowVisible: SHADOWS.small,
              
              headerRight: () => (
                  <Text style={{padding:SIZES.xSmall}}>
                      <Phone/>
                      <Video/>
                  </Text>
              ), 
              // https://reactnavigation.org/docs/headers#replacing-the-title-with-a-custom-component
              headerTitle:route.params.name,
              horizontal:true}
          )
        } 
          component={UserChat} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
