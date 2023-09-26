import { Link, Stack } from 'expo-router';
import { Image, Text, SafeAreaView, Button } from 'react-native';
import Header from '../header/_header';

function Profile() {
    return (
        <SafeAreaView style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            <Header title="profiledbfdijj"></Header>
            <Text>profile Screen</Text>
        </SafeAreaView>
    );
}

export default Profile;