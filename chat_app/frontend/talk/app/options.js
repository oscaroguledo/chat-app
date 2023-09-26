import { Link, Stack } from 'expo-router';
import { Image, Text, SafeAreaView, Button } from 'react-native';
import Header from '../components/header/_header';
import {Icon,Icon2 }from '../components/icon/_icon';

function Options() {
    return (
        <SafeAreaView style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            <Header title="Options"></Header>
            <Icon icon={'setting'} />
            <Icon icon={'contacts'} />
            <Text>Setting Screen</Text>
        </SafeAreaView>
    );
}

export default Options;