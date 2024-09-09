import pandas as pd

def create_output(df):
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])

    # Calculate the datewise total duration for each inside and outside position
    duration_inside = df[df['position'] == 'inside'].groupby([pd.Grouper(key='date')])['datetime'].apply(lambda x: x.max() - x.min()).groupby(level=0).sum()
    duration_outside = df[df['position'] != 'inside'].groupby([pd.Grouper(key='date')])['datetime'].apply(lambda x: x.max() - x.min() if not x.empty else pd.Timedelta(0)).groupby(level=0).sum()

    # Calculate the datewise number of picking and placing activities
    picking_count = df[df['activity'] == 'picked'].groupby('date').size()
    placing_count = df[df['activity'] == 'placed'].groupby('date').size()

    # Combine the results into a single dataframe
    output = pd.DataFrame({
        'date': duration_inside.index,
        'duration_inside': duration_inside.dt.total_seconds() / 3600,
        'duration_outside': duration_outside.dt.total_seconds() / 3600,
        'picking_count': picking_count,
        'placing_count': placing_count
    }).reset_index(drop=True)

    return output

